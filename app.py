import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

const String BUSINESS_NAME = 'J.S. GLOBAL LINKS AND SERVICES';
const String RC_NUMBER = 'BN 8984371';
const String API_KEY = '158b14dc90db48e75971bcd1958f6b5ab41a802737f0892c60b279390b7de665';
const String BASE_URL = 'https://smeplug.com/api/v1';
const String TEST_PHONE_NUMBER = '07062589825';
const int MTN_1GB_PLAN_ID = 1;

void main() { runApp(MyApp()); }

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: HomePage(), debugShowCheckedModeBanner: false);
  }
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String _balance = 'Danna Refresh';
  String _status = 'Shirye don J.S. GLOBAL LINKS';
  bool _loading = false;

  Map<String, String> get headers => {
    'Authorization': 'Bearer $API_KEY',
    'Content-Type': 'application/json',
  };

  Future<void> getBalance() async {
    setState(() { _loading = true; });
    try {
      final res = await http.get(Uri.parse('$BASE_URL/account/balance'), headers: headers);
      if (res.statusCode == 200) {
        final data = jsonDecode(res.body);
        setState(() { _balance = '₦${data['balance']}'; _status = 'An haɗu da SmePlug'; });
      } else {
        setState(() { _status = 'Error: ${res.body}'; });
      }
    } catch (e) {
      setState(() { _status = 'Kuskure: $e'; });
    }
    setState(() { _loading = false; });
  }

  Future<void> buyData() async {
    setState(() { _loading = true; _status = 'Ana aika MTN 1GB zuwa $TEST_PHONE_NUMBER...'; });
    final body = jsonEncode({
      "network_id": 1,
      "plan_id": MTN_1GB_PLAN_ID,
      "phone": TEST_PHONE_NUMBER,
      "customer_reference": "JS_${DateTime.now().millisecondsSinceEpoch}"
    });
    try {
      final res = await http.post(Uri.parse('$BASE_URL/data/purchase'), headers: headers, body: body);
      final data = jsonDecode(res.body);
      setState(() { _status = data['msg'] ?? res.body; });
      getBalance();
    } catch (e) {
      setState(() { _status = 'Kuskure: $e'; });
    }
    setState(() { _loading = false; });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(BUSINESS_NAME)),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(children: [
          Text('RC: $RC_NUMBER'),
          SizedBox(height: 20),
          ListTile(
            title: Text('WALLET BALANCE'),
            subtitle: Text(_balance, style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
            trailing: IconButton(icon: Icon(Icons.refresh), onPressed: getBalance),
          ),
          SizedBox(height: 20),
          ElevatedButton(
            onPressed: _loading ? null : buyData,
            child: Text('Saya MTN 1GB zuwa $TEST_PHONE_NUMBER'),
          ),
          SizedBox(height: 20),
          if (_loading) CircularProgressIndicator(),
          Text('Status: $_status'),
        ]),
      ),
    );
  }
}
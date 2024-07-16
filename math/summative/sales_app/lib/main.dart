import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:iconsax/iconsax.dart';

void main() {
  runApp(const PredictionApp());
}

class PredictionApp extends StatelessWidget {
  const PredictionApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sales Prediction App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const NumberPrediction(),
    );
  }
}

class NumberPrediction extends StatefulWidget {
  const NumberPrediction({super.key});

  @override
  // ignore: library_private_types_in_public_api
  _NumberPredictionState createState() => _NumberPredictionState();
}

class _NumberPredictionState extends State<NumberPrediction> {
  final TextEditingController _controllerTV = TextEditingController();
  final TextEditingController _controllerRadio = TextEditingController();
  final TextEditingController _controllerNewspaper = TextEditingController();
  String _result = '';
  // ignore: prefer_final_fields
  List<String> _history = [];
  bool _isHistoryVisible = true;

  Future<void> _predictNumber() async {
    double tvBudget = double.tryParse(_controllerTV.text) ?? 0.0;
    double radioBudget = double.tryParse(_controllerRadio.text) ?? 0.0;
    double newspaperBudget = double.tryParse(_controllerNewspaper.text) ?? 0.0;

    // Prepare the payload for the API request
    final payload = json.encode({
      'TV_ad_budget': tvBudget,
      'Radio_ad_budget': radioBudget,
      'Newspaper_ad_budget': newspaperBudget,
    });

    try {
      // Make the HTTP request to the endpoint
      final response = await http.post(
        Uri.parse('https://ad-sales-model.onrender.com/predict'),
        headers: {'Content-Type': 'application/json'},
        body: payload,
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        double predicted = data['prediction'];
        String historyEntry =
            'Predicted: TV: ${tvBudget.toStringAsFixed(1)}, Radio: ${radioBudget.toStringAsFixed(1)}, Newspaper: ${newspaperBudget.toStringAsFixed(1)} => Sales Revenue: \$${predicted.toStringAsFixed(2)}';

        setState(() {
          _result = predicted.toStringAsFixed(2);
          _history.add(historyEntry);
        });
      } else {
        setState(() {
          _result = 'Error: ${response.statusCode}';
        });
      }
    } catch (e) {
      setState(() {
        _result = 'Error: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    bool isPortrait =
        MediaQuery.of(context).orientation == Orientation.portrait;

    return Scaffold(
      appBar: AppBar(
        backgroundColor: const Color(0xFF339FFF),
        title: const Text('Sales Prediction App',
            style: TextStyle(color: Colors.white)),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: isPortrait ? _buildPortraitLayout() : _buildLandscapeLayout(),
        ),
      ),
    );
  }

  Widget _buildPortraitLayout() {
    return Column(
      children: [
        Center(
          child: Image(
            image: const AssetImage(
                'assets/thinking.gif'), // Replace with your image path
            width: MediaQuery.of(context).size.width * 0.6,
          ),
        ),
        const SizedBox(height: 16),
        const Text(
          'Sales Prediction',
          style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
          textAlign: TextAlign.center,
        ),
        const SizedBox(height: 8),
        const Text(
          'Enter ad budgets for prediction',
          style: TextStyle(fontSize: 16, fontStyle: FontStyle.italic),
          textAlign: TextAlign.center,
        ),
        const SizedBox(height: 16),

        /// Number Inputs
        TextField(
          controller: _controllerTV,
          keyboardType: TextInputType.number,
          decoration: const InputDecoration(
            prefixIcon: Icon(Iconsax.video),
            labelText: 'Enter TV Ad Budget',
            border: OutlineInputBorder(),
          ),
        ),
        const SizedBox(height: 16),
        TextField(
          controller: _controllerRadio,
          keyboardType: TextInputType.number,
          decoration: const InputDecoration(
            prefixIcon: Icon(Iconsax.radio),
            labelText: 'Enter Radio Ad Budget',
            border: OutlineInputBorder(),
          ),
        ),
        const SizedBox(height: 16),
        TextField(
          controller: _controllerNewspaper,
          keyboardType: TextInputType.number,
          decoration: const InputDecoration(
            prefixIcon: Icon(Iconsax.book),
            labelText: 'Enter Newspaper Ad Budget',
            border: OutlineInputBorder(),
          ),
        ),
        const SizedBox(height: 16),

        /// Predict Button
        SizedBox(
          width: double.infinity,
          child: ElevatedButton(
            onPressed: _predictNumber,
            style: ElevatedButton.styleFrom(
              foregroundColor: Colors.white,
              backgroundColor: const Color(0xFF339FFF),
            ),
            child: const Text('Predict'),
          ),
        ),
        const SizedBox(height: 16),

        /// Result Display
        Text(
          'Sales Revenue: $_result',
          style: const TextStyle(fontSize: 24),
        ),
        const SizedBox(height: 16),

        /// Toggle History Button
        TextButton(
          onPressed: () {
            setState(() {
              _isHistoryVisible = !_isHistoryVisible;
            });
          },
          style: TextButton.styleFrom(
            foregroundColor: const Color(0xFF339FFF),
          ),
          child: Text(_isHistoryVisible ? 'Hide History' : 'Show History'),
        ),
        const SizedBox(height: 16),

        /// History Display
        if (_isHistoryVisible)
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'History:',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              ListView.builder(
                shrinkWrap: true,
                itemCount: _history.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(_history[index]),
                  );
                },
              ),
            ],
          ),
      ],
    );
  }

  Widget _buildLandscapeLayout() {
    return Row(
      children: [
        Expanded(
          child: Column(
            children: [
              Center(
                child: Image(
                  image: const AssetImage(
                      'assets/thinking.gif'), // Replace with your image path
                  width: MediaQuery.of(context).size.width * 0.3,
                ),
              ),
              const SizedBox(height: 16),
              const Text(
                'Sales Prediction',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 8),
              const Text(
                'Enter ad budgets for prediction',
                style: TextStyle(fontSize: 16, fontStyle: FontStyle.italic),
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 16),

              /// Number Inputs
              TextField(
                controller: _controllerTV,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  prefixIcon: Icon(Iconsax.video),
                  labelText: 'Enter TV Ad Budget',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _controllerRadio,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  prefixIcon: Icon(Iconsax.radio),
                  labelText: 'Enter Radio Ad Budget',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _controllerNewspaper,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  prefixIcon: Icon(Iconsax.book),
                  labelText: 'Enter Newspaper Ad Budget',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 16),

              /// Predict Button
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: _predictNumber,
                  style: ElevatedButton.styleFrom(
                    foregroundColor: Colors.white,
                    backgroundColor: const Color(0xFF339FFF),
                  ),
                  child: const Text('Predict'),
                ),
              ),
              const SizedBox(height: 16),

              /// Result Display
              Text(
                'Sales Revenue: $_result',
                style: const TextStyle(fontSize: 24),
              ),
              const SizedBox(height: 16),

              /// Toggle History Button
              TextButton(
                onPressed: () {
                  setState(() {
                    _isHistoryVisible = !_isHistoryVisible;
                  });
                },
                style: TextButton.styleFrom(
                  foregroundColor: const Color(0xFF339FFF),
                ),
                child:
                    Text(_isHistoryVisible ? 'Hide History' : 'Show History'),
              ),
              const SizedBox(height: 16),
            ],
          ),
        ),
        if (_isHistoryVisible)
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'History:',
                  style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                ),
                Expanded(
                  child: ListView.builder(
                    itemCount: _history.length,
                    itemBuilder: (context, index) {
                      return ListTile(
                        title: Text(_history[index]),
                      );
                    },
                  ),
                ),
              ],
            ),
          ),
      ],
    );
  }
}

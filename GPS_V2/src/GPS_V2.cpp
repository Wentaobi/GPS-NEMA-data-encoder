//============================================================================
// Name        : GPS_V2.cpp
// Author      : Wentao
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
/*
GPS data：
$GPGGA,025621.00,2602.33721,N,11911.49176,E,2,04,1.63,13.5,M,9.9,M,,0000*5D
$GPRMC,025622.20,A,2602.33722,N,11911.49176,E,0.100,,281211,,,D*79
 The code is to decode GPS NEMA protocol data to our desired data format, which makes sense.
 I used a string class to read and shift string. read one by one.
*/
#include<stdio.h>
#include<fstream>
#include<string>
#include<iostream>
#include<vector>
#include<sstream>
#include<math.h>
using namespace std;

//Data type conversion template functions
template <class Type>
Type stringToNum(const string str)
{
	istringstream iss(str);
	Type num;
	iss >> num;
	return num;
}

int main()
{
	ifstream is("gpstest.txt");
	string line,line1,line2;
	getline(is,line);
	line1 = line;
	//========================= GPGGA format
	//Read the first line GPGGA format  $GPGGA,025620.00,2602.33721,N,11911.49176,E,2,04,1.63,13.5,M,9.9,M,,0000*5D
	//Define a string container
	vector<string> arr1;
	int position = 0;
	do
	{
		string tmp_s;
		//Find the comma's location
		position = line.find(",");
		//Interception of the required string
		tmp_s = line.substr(0,position);
		//Delete the data already read
		line.erase(0,position+1);
		//Pressed the string into the container
		arr1.push_back(tmp_s);
	}while(position != -1);

		//Constructs a datetime string YYYY-MM-DD HH:MM:SS
		string datetime = arr1[1].substr(0,2)+":"+arr1[1].substr(2,2)+":"+arr1[1].substr(4,2);
		cout<<arr1[0]<<" Format "<<line1<<endl;
		cout<<"UTC time："<<datetime<<endl;
		double d0 = stringToNum<double>(arr1[2]);
		// longitude: ddmm.mmmm
		cout<<arr1[3]<<' '<<"longitude：";
		double d0_mod = fmod(d0, 100)/60;
		int d0_int = floor(d0 / 100);
		printf("%lf\n", d0_mod + d0_int);
		//if use cout, valid digits will lose
		double d1 = stringToNum<double>(arr1[4]);
		double d1_mod = fmod(d1, 100)/60;
		int d1_int = floor(d1 / 100);
		cout<<arr1[5]<<' '<<"latitude：";
		printf("%lf\n", d1_mod + d1_int);
		cout<<"GPS type: ";
		switch (stringToNum<int>(arr1[6]))
		{
		case 0:
			printf("Not located \n");
			break;
		case 1:
			printf("Not Didderential GPS \n");
			break;
		case 2:
			printf("Didderential GPS \n");
			break;
		case 6:
			printf("Now config-ing \n");
			break;
		default:
			break;
		}
		cout<<"GPS amount："<<stringToNum<int>(arr1[7])<<endl;
		cout<<"HDOP："<<(arr1[8])<<endl;
		cout<<"Units："<<(arr1[10])<<endl;
		cout<<"altitude："<<arr1[9]<<arr1[10]<<endl;
		cout<<"Age of Diff. Corr："<< (arr1[11]) <<endl;
		cout<<"Diff. Ref. Station ID："<< arr1[14].substr(0,4) <<endl;
		cout<<"Checksum："<< arr1[14].substr(5,6) <<endl;
	//	return 0;
	// $GPRMC,025622.20,A,2602.33722,N,11911.49176,E,0.100,,281211,,,D*79
	position = 0;
	getline(is,line);
	line2 = line;
	//Read the second line RMC format  $GPRMC,025620.20,A,2602.33722,N,11911.49176,E,0.100,,281211,,,D*79

	vector<string> arr2;
	do
	{
		string tmp_s;
		position = line.find(",");  //Find the comma's location
		tmp_s = line.substr(0,position);  //Interception of the required string
		line.erase(0,position+1);  //Delete the data already read
		arr2.push_back(tmp_s); //Pressed the string into the container
	}while(position != -1);
	is.close();
	printf("\n");
	cout<<arr1[0]<<" Format "<<line2<<endl;
	//Constructs a datetime string YYYY-MM-DD HH:MM:SS
	string datetime2 = "20"+arr2[9].substr(4,2)+"-"+arr2[9].substr(2,2)+"-"+arr2[9].substr(0,2)+" "+arr2[1].substr(0,2)+
		":"+arr2[1].substr(2,2)+":"+arr2[1].substr(4,2);
	cout<<"UTC time："<<datetime2<<endl;
	cout<<"GPS state："<<arr2[2]<<endl;
	double d20 = stringToNum<double>(arr2[3]);
	cout<<"longitude：";
	double d20_mod = fmod(d20, 100)/60;
	int d20_int = floor(d20 / 100);
	printf("%lf\n", d20_mod + d20_int);

	double d21 = stringToNum<double>(arr2[5]);
	double d21_mod = fmod(d21, 100)/60;
	int d21_int = floor(d21 / 100);
	cout<<arr2[6]<<' '<<"latitude：";
	printf("%lf\n", d21_mod + d21_int);
	double d27 = stringToNum<double>(arr2[7]);
	cout<<"Speed over ground："<<d27*1.852/3.6<<" m/s"<<endl;
	cout<<"GPS mode："<<arr2[12].substr(0,1)<<endl;
	cout<<"Check-sum："<<arr2[12].substr(2,4)<<endl;
	return 0;

}
/*
 *result
$GPGGA Format $GPGGA,025621.00,2602.33721,N,11911.49176,E,1,04,1.63,13.5,M,,,,0000*5D
UTC time：02:56:21
N longitude：26.038954
E latitude：119.191529
GPS type: Not Didderential GPS
GPS amount：4
HDOP：1.63
Units：M
altitude：13.5M
Age of Diff. Corr：
Diff. Ref. Station ID：0000
Checksum：5D

$GPGGA Format $GPRMC,025622.20,A,2602.33722,N,11911.49176,E,0.100,,281211,,,D*79
UTC time：2011-12-28 02:56:22
GPS state：A
longitude：26.038954
E latitude：119.191529
Speed over ground：0.0514444 m/s
GPS mode：D
Check-sum：79
 *
 */


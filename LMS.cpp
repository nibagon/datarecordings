#include "Fir1.h"
#include "Iir.h"
//#include <butterworth.h> not necessary 

#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define NTAPS 250//250
#define LEARNING_RATE 0.5//fid a way of calculating this learning rate 0.5 bicep

int main (int,char**)
{
	// inits the filter
	Fir1 fir(NTAPS);
	fir.setLearningRate(LEARNING_RATE);
	double errorGain=1;//ECG
	double outputGain=100000;//EMG
//
	FILE *finput1 = fopen("data/lastrecordings/armn.dat","rt");//the nice one
    FILE *foutput1 = fopen("Results/Last_recordings/LMS/armn.dat","wt");
	//with weight
	FILE *finput2 = fopen("data/lastrecordings/Weightarm.dat","rt");//the nice one
    FILE *foutput2= fopen("Results/Last_recordings/LMS/Weightarm.dat","wt");
//bicep
	FILE *finput3 = fopen("data/lastrecordings/bicep.dat","rt");//the nice one
    FILE *foutput3 = fopen("Results/Last_recordings/LMS/bicep.dat","wt");
	//with weight
	FILE *finput4 = fopen("data/lastrecordings/WeightB.dat","rt");//the nice one
    FILE *foutput4 = fopen("Results/Last_recordings/LMS/Weightb.dat","wt");
	//old
	FILE *finput5 = fopen("data/data2.21/bicep0.dat","rt");//the nice one
    FILE *foutput5= fopen("Results/2.21/LMS/bicep0.dat","wt");
	for(int i=0;;i++) 
	{
		float ECG=0;
        float EMG=0;	
		float time=0;	
		if (fscanf(finput1,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;

        double emg=0;
        double ecg=0;

        emg=EMG;
        ecg=ECG;

		if (time > 10) {
		double canceller = fir.filter(emg)*outputGain; 
		double output_signal = (ecg - canceller)*errorGain;
		fir.lms_update(output_signal);
										  //0  , 1                       ,2                  ,3  ,4 
		fprintf(foutput1,"%e %e %e %e %e\n",time,output_signal/errorGain,canceller/outputGain,ECG,EMG);
		}
	}
	fclose(finput1);
    //fclose(noise);
	fclose(foutput1);
	fprintf(stderr,"FILE 1 done'\n");
		for(int i=0;;i++) 
	{
		float ECG=0;
        float EMG=0;	
		float time=0;	
		if (fscanf(finput2,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;

        double emg=0;
        double ecg=0;

        emg=EMG;
        ecg=ECG;

		if (time > 10) {
		double canceller = fir.filter(emg)*outputGain; 
		double output_signal = (ecg - canceller)*errorGain;
		fir.lms_update(output_signal);
										  //0  ,1                 ,2             ,3  ,4 
		fprintf(foutput2,"%e %e %e %e %e\n",time,output_signal/errorGain,canceller/outputGain,ECG,EMG);
		}
	}
	fclose(finput2);
    //fclose(noise);
	fclose(foutput2);
	fprintf(stderr,"FILE 2 done'\n");
		for(int i=0;;i++) 
	{
		float ECG=0;
        float EMG=0;	
		float time=0;	
		if (fscanf(finput3,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;

        double emg=0;
        double ecg=0;

        emg=EMG;
        ecg=ECG;

		if (time > 10) {
		double canceller = fir.filter(emg)*outputGain; 
		double output_signal = (ecg - canceller)*errorGain;
		fir.lms_update(output_signal);
										  //0  ,1                 ,2             ,3  ,4 
		fprintf(foutput3,"%e %e %e %e %e\n",time,output_signal/errorGain,canceller/outputGain,ECG,EMG);
		}
	}
	fclose(finput3);
    //fclose(noise);
	fclose(foutput3);
	fprintf(stderr,"FILE 3 done'\n");
		for(int i=0;;i++) 
	{
		float ECG=0;
        float EMG=0;	
		float time=0;	
		if (fscanf(finput4,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;

        double emg=0;
        double ecg=0;

        emg=EMG;
        ecg=ECG;

		if (time > 10) {
		double canceller = fir.filter(emg)*outputGain; 
		double output_signal = (ecg - canceller)*errorGain;
		fir.lms_update(output_signal);
										  //0  ,1                         ,2                  ,3  ,4 
		fprintf(foutput4,"%e %e %e %e %e\n",time,output_signal/errorGain,canceller/outputGain,ECG,EMG);
		}
	}
	fclose(finput4);
    //fclose(noise);
	fclose(foutput4);
	fprintf(stderr,"FILE 4 done'\n");
		for(int i=0;;i++) 
	{
		float ECG=0;
        float EMG=0;	
		float time=0;	
		if (fscanf(finput5,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;

        double emg=0;
        double ecg=0;

        emg=EMG;
        ecg=ECG;

		if (time > 10) {
		double canceller = fir.filter(emg)*outputGain; 
		double output_signal = (ecg - canceller)*errorGain;
		fir.lms_update(output_signal);
										  //0  ,1                         ,2                  ,3  ,4 
		fprintf(foutput5,"%e %e %e %e %e\n",time,output_signal/errorGain,canceller/outputGain,ECG,EMG);
		}
	}
	fclose(finput5);
    //fclose(noise);
	fclose(foutput5);
	fprintf(stderr,"FILE 5 done'\n");
}
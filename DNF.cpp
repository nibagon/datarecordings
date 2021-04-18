// inclide the fir library
#include "Fir1.h"
#include "Iir.h"
#include "clBP/include/clbp/Neuron.h"
#include "clBP/include/clbp/Layer.h"
#include "clBP/include/clbp/Net.h"
#include "parameters2.h"

//#include <butterworth.h> not necessary 

#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <cassert> 
/*
#define NTAPS 100
#define LEARNING_RATE 0.05//fid a way of calculating this learning rate 
*/
int main (int,char**)
{
	int totalNINPUTS = NINPUTS;
	//initialise network
	int nNeurons[NLAYERS]={N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11};//N7,N8,N9};//change this for th eno. of neurons
	int* nNeuronsp=nNeurons;
	Net* net = new Net(NLAYERS, nNeuronsp, totalNINPUTS);

	// define gains
	double errorGain = 10;
	double outputGain = 1; //0.005; changes 0.000005 with 6 0.0000000005
	
	//initialise the network
    net->initNetwork(Neuron::W_RANDOM, Neuron::B_NONE, Neuron::Act_Sigmoid); 
    net->setLearningRate(LEARNINGRATE);

	//buffer for the network inputs
	double inputsDelayed[totalNINPUTS]={0};
	//arm
	FILE *finput1 = fopen("data/lastrecordings/armn.dat","rt");//where data is extracted
    FILE *foutput1 = fopen("Results/Last_recordings/DNF/armn.dat","wt");//where data is saved
	FILE *finput2 = fopen("data/lastrecordings/Weightarm.dat","rt");//where data is extracted
    FILE *foutput2 = fopen("Results/Last_recordings/DNF/Weightarm.dat","wt");//where data is saved
	//bicep
	FILE *finput3 = fopen("data/lastrecordings/bicep.dat","rt");//where data is extracted
    FILE *foutput3 = fopen("Results/Last_recordings/DNF/bicep.dat","wt");//where data is saved
	FILE *finput4 = fopen("data/lastrecordings/WeightB.dat","rt");//where data is extracted
    FILE *foutput4 = fopen("Results/Last_recordings/DNF/WeightB.dat","wt");//where data is saved
	//old
	FILE *finput5 = fopen("data/data2.21/bicep0.dat","rt");//where data is extracted
    FILE *foutput5 = fopen("Results/2.21/DNF/bicep0.dat","wt");//where data is saved
	for(int i=0;;i++) 
	{
		float ECG=0;
        float EMG=0;	
		float time=0;	
		if (fscanf(finput1,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;
		double ecg=0;
        double emg=0;

		ecg= ECG;
		emg= EMG;
		assert(isfinite(ecg) && isfinite(emg));

		if (time > 10) {
		/*	
		double canceller = fir.filter(emg_high); 
		double output_signal = ecg_high - canceller;
		fir.lms_update(output_signal);*/
		
	    
		for (int i=totalNINPUTS; i>0; i--){
        	inputsDelayed[i]=inputsDelayed[i-1];
        }
		inputsDelayed[0]=emg;
		//propagate the inputs
        double* inputsDelayedPointer = &inputsDelayed[0];
        net->setInputs(inputsDelayedPointer);
        net->propInputs();
        //get the network's output
        double outPut = net->getOutput(0) * outputGain;
		assert(isfinite(outPut));
        //workout the error
        double leadError = (ecg - outPut) * errorGain;
        //propagate the error
        net->setError(leadError);
        net->propError();
        //do learning on the weights
        net->updateWeights();
        //net->saveWeights();
        double weightDist = net->getWeightDistance();
										   //0  ,1        ,2     ,3  ,4       ,5  ,6 
		fprintf(foutput1,"%e %e %e %e %e\n",time,leadError/errorGain,outPut/outputGain,ECG,EMG);
		}
		
	}
	fclose(finput1);
    //fclose(noise);
	fclose(foutput1);
	fprintf(stderr,"file 1 ready'\n");
	for(int i=0;;i++) 
	{
		float ECG=0;
        float EMG=0;	
		float time=0;	
		if (fscanf(finput2,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;
		double ecg=0;
        double emg=0;

		ecg= ECG;
		emg= EMG;
		assert(isfinite(ecg) && isfinite(emg));

		if (time > 10) {
		/*	
		double canceller = fir.filter(emg_high); 
		double output_signal = ecg_high - canceller;
		fir.lms_update(output_signal);*/
		
	    
		for (int i=totalNINPUTS; i>0; i--){
        	inputsDelayed[i]=inputsDelayed[i-1];
        }
		inputsDelayed[0]=emg;
		//propagate the inputs
        double* inputsDelayedPointer = &inputsDelayed[0];
        net->setInputs(inputsDelayedPointer);
        net->propInputs();
        //get the network's output
        double outPut = net->getOutput(0) * outputGain;
		assert(isfinite(outPut));
        //workout the error
        double leadError = (ecg - outPut) * errorGain;
        //propagate the error
        net->setError(leadError);
        net->propError();
        //do learning on the weights
        net->updateWeights();
        //net->saveWeights();
        double weightDist = net->getWeightDistance();
										   //0  ,1        ,2     ,3  ,4       ,5  ,6 
		fprintf(foutput2,"%e %e %e %e %e\n",time,leadError/errorGain,outPut/outputGain,ECG,EMG);
		}
		
	}
	fclose(finput2);
    //fclose(noise);
	fclose(foutput2);
	fprintf(stderr,"file 1 ready'\n");
	for(int i=0;;i++) 
	{
		float ECG=0;
        float EMG=0;	
		float time=0;	
		if (fscanf(finput3,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;
		double ecg=0;
        double emg=0;

		ecg= ECG;
		emg= EMG;
		assert(isfinite(ecg) && isfinite(emg));

		if (time > 10) {
		/*	
		double canceller = fir.filter(emg_high); 
		double output_signal = ecg_high - canceller;
		fir.lms_update(output_signal);*/
		
	    
		for (int i=totalNINPUTS; i>0; i--){
        	inputsDelayed[i]=inputsDelayed[i-1];
        }
		inputsDelayed[0]=emg;
		//propagate the inputs
        double* inputsDelayedPointer = &inputsDelayed[0];
        net->setInputs(inputsDelayedPointer);
        net->propInputs();
        //get the network's output
        double outPut = net->getOutput(0) * outputGain;
		assert(isfinite(outPut));
        //workout the error
        double leadError = (ecg - outPut) * errorGain;
        //propagate the error
        net->setError(leadError);
        net->propError();
        //do learning on the weights
        net->updateWeights();
        //net->saveWeights();
        double weightDist = net->getWeightDistance();
										   //0  ,1        ,2     ,3  ,4       ,5  ,6 
		fprintf(foutput3,"%e %e %e %e %e\n",time,leadError/errorGain,outPut/outputGain,ECG,EMG);
		}
		
	}
	fclose(finput3);
    //fclose(noise);
	fclose(foutput3);
	fprintf(stderr,"file 1 ready'\n");
	for(int i=0;;i++) 
	{
		float ECG=0;
        float EMG=0;	
		float time=0;	
		if (fscanf(finput4,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;
		double ecg=0;
        double emg=0;

		ecg= ECG;
		emg= EMG;
		assert(isfinite(ecg) && isfinite(emg));

		if (time > 10) {
		/*	
		double canceller = fir.filter(emg_high); 
		double output_signal = ecg_high - canceller;
		fir.lms_update(output_signal);*/
		
	    
		for (int i=totalNINPUTS; i>0; i--){
        	inputsDelayed[i]=inputsDelayed[i-1];
        }
		inputsDelayed[0]=emg;
		//propagate the inputs
        double* inputsDelayedPointer = &inputsDelayed[0];
        net->setInputs(inputsDelayedPointer);
        net->propInputs();
        //get the network's output
        double outPut = net->getOutput(0) * outputGain;
		assert(isfinite(outPut));
        //workout the error
        double leadError = (ecg - outPut) * errorGain;
        //propagate the error
        net->setError(leadError);
        net->propError();
        //do learning on the weights
        net->updateWeights();
        //net->saveWeights();
        double weightDist = net->getWeightDistance();
										   //0  ,1        ,2     ,3  ,4       ,5  ,6 
		fprintf(foutput4,"%e %e %e %e %e\n",time,leadError/errorGain,outPut/outputGain,ECG,EMG);
		}
		
	}
	fclose(finput4);
    //fclose(noise);
	fclose(foutput4);
	fprintf(stderr,"file 1 ready'\n");
	for(int i=0;;i++) 
	{
		float ECG=0;
        float EMG=0;	
		float time=0;	
		if (fscanf(finput5,"%e\t%e\t%e\n" ,&time,&ECG,&EMG)<1) break;
		double ecg=0;
        double emg=0;

		ecg= ECG;
		emg= EMG;
		assert(isfinite(ecg) && isfinite(emg));

		if (time > 10) {
		/*	
		double canceller = fir.filter(emg_high); 
		double output_signal = ecg_high - canceller;
		fir.lms_update(output_signal);*/
		
	    
		for (int i=totalNINPUTS; i>0; i--){
        	inputsDelayed[i]=inputsDelayed[i-1];
        }
		inputsDelayed[0]=emg;
		//propagate the inputs
        double* inputsDelayedPointer = &inputsDelayed[0];
        net->setInputs(inputsDelayedPointer);
        net->propInputs();
        //get the network's output
        double outPut = net->getOutput(0) * outputGain;
		assert(isfinite(outPut));
        //workout the error
        double leadError = (ecg - outPut) * errorGain;
        //propagate the error
        net->setError(leadError);
        net->propError();
        //do learning on the weights
        net->updateWeights();
        //net->saveWeights();
        double weightDist = net->getWeightDistance();
										   //0  ,1        ,2     ,3  ,4       ,5  ,6 
		fprintf(foutput5,"%e %e %e %e %e\n",time,leadError/errorGain,outPut/outputGain,ECG,EMG);
		}
		
	}
	fclose(finput5);
    //fclose(noise);
	fclose(foutput5);
	fprintf(stderr,"file 1 ready'\n");
	return 0;
}
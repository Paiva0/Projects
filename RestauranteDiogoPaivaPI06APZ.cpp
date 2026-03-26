#include <iostream>
#include <vector>
using namespace std;

vector<int> precosPratos = {0,5,8,4,3};
vector<int> precosSobremesas = {0,3,4};
vector<int> precosBebidas = {0,2,3,1};

vector<float> totais = {0,0,0,0,0};

int escolherMesa() {
	int mesa;
	cout << "Escolhe a mesa (1-4): ";
	cin >> mesa;

	if (mesa < 1 || mesa > 4) {
		cout << "Mesa invalida. A usar mesa 1.\n";
		mesa = 1;
	}

	return mesa;
}

void menuG() {
	cout<<"\n1 - Pratos\n";
	cout<<"2 - Sobremesas\n";
	cout<<"3 - Bebidas\n";
}

void menuR() {
	cout<<"\n1 - Hamburguer (5 euros)\n";
	cout<<"2 - Pizza (8 euros)\n";
	cout<<"3 - Salada (4 euros)\n";
	cout<<"4 - Batatas fritas (3 euros)\n";
}

void menuS() {
	cout<<"\n1 - Gelado (3 euros)\n";
	cout<<"2 - Bolo (4 euros)\n";
}

void menuB() {
	cout<<"\n1 - Refrigerante (2 euros)\n";
	cout<<"2 - Vinho (3 euros)\n";
	cout<<"3 - Agua (1 euro)\n";
}

void adicionar(int mesa) {
	int tipo;
	menuG();
	cout<<"Escolha o tipo: ";
	cin>>tipo;

	int item;

	if(tipo==1) {
		menuR();
		cout<<"Escolha: ";
		cin>>item;

		if(item<1 || item>4) {
			cout<<"Item invalido\n";
			return;
		}

		totais[mesa]+=precosPratos[item];
	}

	else if(tipo==2) {
		menuS();
		cout<<"Escolha: ";
		cin>>item;

		if(item<1 || item>2) {
			cout<<"Item invalido\n";
			return;
		}

		totais[mesa]+=precosSobremesas[item];
	}

	else if(tipo==3) {
		menuB();
		cout<<"Escolha: ";
		cin>>item;

		if(item<1 || item>3) {
			cout<<"Item invalido\n";
			return;
		}

		totais[mesa]+=precosBebidas[item];
	}

	else {
		cout<<"Opcao invalida\n";
		return;
	}

	cout<<"Total mesa "<<mesa<<": "<<totais[mesa]<<" euros\n";
}

void remover(int mesa) {
	int tipo;
	menuG();
	cout<<"Escolha o tipo a remover: ";
	cin>>tipo;

	int item;
	int preco=0;

	if(tipo==1) {
		menuR();
		cout<<"Escolha: ";
		cin>>item;

		if(item<1 || item>4) {
			cout<<"Item invalido\n";
			return;
		}

		preco=precosPratos[item];
	}

	else if(tipo==2) {
		menuS();
		cout<<"Escolha: ";
		cin>>item;

		if(item<1 || item>2) {
			cout<<"Item invalido\n";
			return;
		}

		preco=precosSobremesas[item];
	}

	else if(tipo==3) {
		menuB();
		cout<<"Escolha: ";
		cin>>item;

		if(item<1 || item>3) {
			cout<<"Item invalido\n";
			return;
		}

		preco=precosBebidas[item];
	}

	else {
		cout<<"Opcao invalida\n";
		return;
	}

	if(totais[mesa]-preco<0) {
		cout<<"Nao e possivel remover\n";
		return;
	}

	totais[mesa]-=preco;

	cout<<"Total mesa "<<mesa<<": "<<totais[mesa]<<" euros\n";
}

float desconto(float total) {
	return total*0.9;
}

int main() {
	int opcao;
	int mesa=1;

	do {
		cout<<"\n--- RESTAURANTE ---\n";
		cout<<"1 - Escolher mesa\n";
		cout<<"2 - Adicionar item\n";
		cout<<"3 - Remover item\n";
		cout<<"4 - Ver total da mesa\n";
		cout<<"5 - Ver total de todas as mesas\n";
		cout<<"6 - Ver total com desconto\n";
		cout<<"7 - Reset a mesa\n";
		    cout<<"0 - Sair\n";
		cout<<"Opcao: ";
		cin>>opcao;

		switch(opcao) {

		case 1:
			mesa=escolherMesa();
			cout<<"Mesa "<<mesa<<" selecionada\n";
			break;

		case 2:
			mesa=escolherMesa();
			adicionar(mesa);
			break;

		case 3:
			mesa=escolherMesa();
			remover(mesa);
			break;

		case 4:
			mesa=escolherMesa();
			cout<<"Total mesa "<<mesa<<": "<<totais[mesa]<<" euros\n";
			break;

		case 5: {
			float total=0;
			for(float t:totais)
				total+=t;

			cout<<"Total de todas as mesas: "<<total<<" euros\n";
			break;
		}

		case 6:
			mesa=escolherMesa();
			cout<<"Total com desconto: "<<desconto(totais[mesa])<<" euros\n";
			break;

		case 7:
		{
			int reset;
			cout << "Que mesa quer dar reset? ";
			cin >> reset;

			switch(reset) {
			case 1:
				totais[1] = 0;
				cout<<"Mesa 1 reseted";
				break;
			case 2:
				totais[2] = 0;
				cout<<"Mesa 2 reseted";
				break;
			case 3:
				totais[3] = 0;				
				cout<<"Mesa 3 reseted";
				break;
			case 4:
				totais[4] = 0;
				cout<<"Mesa 4 reseted";
				break;
			default:
				cout << "Mesa invalida\n";
			}

			break;
		}


		case 0:
			cout<<"A sair...\n";
			break;
		}

	} while(opcao!=0);

	return 0;
}
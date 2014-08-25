package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
)

func limpiarPantalla() {
	var cmd *exec.Cmd
	if runtime.GOOS == "windows" {
		cmd = exec.Command("cmd", "/c", "cls")
	} else {
		cmd = exec.Command("clear")
	}
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func inicio() {
	limpiarPantalla()
}

func mostrarMenues(menu int) string{
	if menu == 1 {
		menuUno()
	} else if menu == 2 {
		menuArit()
	} else if menu == 3 {
		menuGeom()
	}
	opc, _ := readString("")
	return opc
}

func ejecutarAccion(menu int, opcion string) int {
	if menu == 1 {
		if opcion == "1" {
			menu = 2 //Cambiamos al menu aritmetico
		} else if opcion == "2" {
			menu = 3 //Cambiamos al menu geometrico
		} else if opcion == "99" {
			menu = 0 //Ponemos menu en 0 para terminar el programa
		}
	} else if menu == 2 {
		if opcion == "1" {
			suma() //Suma
		} else if opcion == "2" {
			multiplicacion()
		} else if opcion == "99" {
			menu = 1
		}
	} else if menu == 3 {
		if opcion == "1" {
			areaRect() //Suma
		} else if opcion == "2" {
			areaCirc()
		} else if opcion == "99" {
			menu = 1
		}
	}
	return menu
}


////////////////// Menues /////////////////////////////////////////

func menuUno(){
    limpiarPantalla()
    fmt.Println("Menu Principal:")
    fmt.Println("	1  - Menu aritmetico")
    fmt.Println("	2  - Menu geometrico")
    fmt.Println("	99 - Salir")
}

func menuArit(){
    limpiarPantalla()
    fmt.Println("Menu Aritmetico:")
    fmt.Println("	1  - Suma")
    fmt.Println("	2  - Multiplicacion")
    fmt.Println("	99 - Menu principal")    
}

func menuGeom(){
    limpiarPantalla()
    fmt.Println("Menu Geométrico:")
    fmt.Println("	1  - Area rectangulo")
    fmt.Println("	2  - Area circulo")
    fmt.Println("	99 - Menu principal")  
}


////////////////// Acciones ////////////////////////////////////

func readNumber(text string) (float64, error) {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(text)
	textr, _ := reader.ReadString('\n')
	return strconv.ParseFloat(strings.TrimSpace(textr), 64)
}

func readString(text string) (string, error){
	reader := bufio.NewReader(os.Stdin)
	if (text != ""){
		fmt.Print(text)
	}
	t, e := reader.ReadString('\n')
	return  strings.TrimSpace(t), e
}

func suma(){
    limpiarPantalla()
	v1, _ := readNumber("Ingrese primer valor: ")
	v2, _ := readNumber("Ingrese segundo valor: ")
	fmt.Printf("%f + %f = %f \n" ,  v1, v2, v1 + v2)
    readString("Presione cualquier tecla y enter para seguir....")
}

func multiplicacion(){
    limpiarPantalla()
	v1, _ := readNumber("Ingrese primer valor: ")
	v2, _ := readNumber("Ingrese segundo valor: ")
	fmt.Printf("%f * %f = %f \n" ,  v1, v2, v1 * v2)
    readString("Presione cualquier tecla y enter para seguir....")
}

func areaCirc(){
    limpiarPantalla()
	v1, _ := readNumber("Ingrese el radio: ")
    fmt.Printf("%f * %f * Pi  = %f \n" ,  v1, v1, v1 * v1 * 3.1416)
    readString("Presione cualquier tecla y enter para seguir....")
}

func areaRect(){
    limpiarPantalla()
	v1, _ := readNumber("Ingrese el largo: ")
	v2, _ := readNumber("Ingrese el ancho: ")
	fmt.Printf("%f * %f = %f \n" ,  v1, v2, v1 * v2)
    readString("Presione cualquier tecla y enter para seguir....")
}
	

func main() {
	
	var menu int = 1
	var terminar bool = false
	inicio()
	
	for !terminar {
		opcion := mostrarMenues(menu)
		menu = ejecutarAccion(menu, opcion)
		terminar = (menu == 0)
	}
	
}

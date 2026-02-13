public class Main {

    public static void main(String[] args) {

        SensorVoltaje s1 = new SensorVoltaje();
        SensorCorriente s2 = new SensorCorriente();

        s1.medir();
        s2.medir();

        System.out.println("Datos registrados por patron Singleton");
    }
}
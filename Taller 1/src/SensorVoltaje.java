public class SensorVoltaje {

    public void medir() {
        double voltaje = 120.5;

        DataLogger logger = DataLogger.getInstance();
        logger.log("Voltaje: " + voltaje + " V");
    }
}
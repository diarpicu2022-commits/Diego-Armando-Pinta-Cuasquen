public class SensorCorriente {

    public void medir() {
        double corriente = 5.2;

        DataLogger logger = DataLogger.getInstance();
        logger.log("Corriente: " + corriente + " A");
    }
}
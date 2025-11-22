from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Create a SilverServiceTaxi, drive it 18 km, print details and assert the correct fare."""
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    print(hummer)
    hummer.drive(18)
    print(hummer)
    print(f"Fare for 18km Hummer trip = ${hummer.get_fare():.2f}")

    # assert hummer.get_fare() == 48.78, f"Expected $48.78, got ${hummer.get_fare():.2f}"
    assert hummer.get_fare() == 48.80, f"Expected $48.80, got ${hummer.get_fare():.2f}"


main()

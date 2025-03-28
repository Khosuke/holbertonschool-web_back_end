export default class Car {
  constructor(brand = undefined, motor = undefined, cycle = undefined) {
    this._brand = brand;
    this._motor = motor;
    this._cycle = cycle;
  }

  cloneCar() {
    return new this.constructor();
  }
}

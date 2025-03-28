export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Parent must implement evacuationWarningMessage');
    }
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}

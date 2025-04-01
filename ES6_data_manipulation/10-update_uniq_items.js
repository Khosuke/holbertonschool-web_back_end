export default function updateUniqueItems(aMap) {
  if (!(aMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  aMap.forEach((value, key, map) => {
    if (value === 1) {
      map.set(key, 100);
    }
  });

  return aMap;
}

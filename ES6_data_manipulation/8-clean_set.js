export default function cleanSet(set, startString) {
  let cleaned = '';
  for (const element of set) {
    if (element.startsWith(startString)) {
      cleaned += `${element.slice(startString.length)}-`;
    }
  }
  return cleaned.slice(0, -1);
}

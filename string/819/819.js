var mostCommonWord = function(paragraph, banned) {
  const bannedSet = new Set(banned);
  let paragraphClean = paragraph.replace(/[!?',;.]/g, " ").toLowerCase();

  let counter = {};
  for (let word of paragraphClean.split(/\s+/)) {
    if (!counter[word]) {
      counter[word] = 0;
    }
    counter[word]++;
  }
  let max = 0;
  let result = "";
  for (let [word, freq] of Object.entries(counter)) {
    if (freq > max && !bannedSet.has(word)) {
      max = freq;
      result = word;
    }
  }
  return result;
};

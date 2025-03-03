
all: en2fr

raw_verbs:
	pdftotext verbs_all_0.pdf $@

.PHONY: verbs
verbs: raw_verbs
	sed -Ef filter.sed $< > $@

.PHONY: infinitives
infinitives: verbs
	sed '/^voyager$$/q' $< | awk '{print "infinitive:" $$0}' > $@

.PHONY: conjugated_verbs
conjugated_verbs: verbs
	sed -n '/^présent$$/,$$p' $< > $@

.PHONY: conj_verbs_w_pronoun
conj_verbs_w_pronoun: conjugated_verbs
	./add_pronoun.py < $< > $@

.PHONY: fr2en
fr2en: conj_verbs_w_pronoun infinitives
	cat $^ | ./translate.sh > $@

.PHONY: en2fr
en2fr: fr2en
	awk -F: '{printf "%s:%s:%s:%s\n", $1, $3, $2, $4}' $< > $@

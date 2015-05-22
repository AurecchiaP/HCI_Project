section_homepage_main.jinja
{{ sectionTitle }}				Title of the section
{{ sectionDescription }}		Description
{{ sectionClass }}				Class of the section, controls entry borders,
								acceptable values: Internet, Games, Hardware, Software, HCI
{{ timelineEntries }}			All the entries of the timeline, using timeline_entry.jinja

timeline_entry.jinja
{{ entryLink }}					Path to the page
{{ entryImage }}				Path to the image
{{ entryTitle }}				Page title
{{ entryDate }}					Page date
{{ entryDescription }}			Page description

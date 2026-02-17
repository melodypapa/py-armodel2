Let us to implement how to read and write the `demos/arxml/AUTOSAR_Datatypes.arxml`


**Documentation**

1. Design the requirements and unit test cases first 
2. Update the requirements and unit test in the `docs` 
3. One integration test shall be design and update in the `docs/tests/integration`
   - Read and write the arxml
   - write the arxml to another file and compare them with file to ensure the implementation is correct.

**Implementation**
1. Use the TDD methodlogy to implement this feature
2. Collect the related classes which shall be use in this arxml into one markdown file.
3. Update these related classes hierachy with `docs/json/hierarchy.json` 
4. Update these related classes with the followin json files.
   - the class related information can be read from `docs/json/packages` and `mapping.json`
   - the members' name shall be check with arxml file. If any conflict, report and update the python member name.
   - the members type is any (...) can be considered the type is known, needs to be analyzed. report and provide your recommendation
5. Implement the serialize for each classes
6. Implement the reader and writer to handle the arxml.
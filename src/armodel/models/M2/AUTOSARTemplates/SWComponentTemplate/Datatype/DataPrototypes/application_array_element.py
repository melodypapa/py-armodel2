"""ApplicationArrayElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 252)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 43)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import (
    ApplicationCompositeElementDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArraySizeSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ArraySizeHandlingEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )



class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    """AUTOSAR ApplicationArrayElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_size_handling: Optional[ArraySizeHandlingEnum]
    array_size_semantics: Optional[ArraySizeSemanticsEnum]
    index_data_type_ref: Optional[ARRef]
    max_number_of_elements: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ApplicationArrayElement."""
        super().__init__()
        self.array_size_handling: Optional[ArraySizeHandlingEnum] = None
        self.array_size_semantics: Optional[ArraySizeSemanticsEnum] = None
        self.index_data_type_ref: Optional[ARRef] = None
        self.max_number_of_elements: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationArrayElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationArrayElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_size_handling
        if self.array_size_handling is not None:
            serialized = SerializationHelper.serialize_item(self.array_size_handling, "ArraySizeHandlingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE-HANDLING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize array_size_semantics
        if self.array_size_semantics is not None:
            serialized = SerializationHelper.serialize_item(self.array_size_semantics, "ArraySizeSemanticsEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE-SEMANTICS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize index_data_type_ref
        if self.index_data_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.index_data_type_ref, "ApplicationPrimitiveDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDEX-DATA-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_number_of_elements
        if self.max_number_of_elements is not None:
            serialized = SerializationHelper.serialize_item(self.max_number_of_elements, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF-ELEMENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationArrayElement":
        """Deserialize XML element to ApplicationArrayElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationArrayElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationArrayElement, cls).deserialize(element)

        # Parse array_size_handling
        child = SerializationHelper.find_child_element(element, "ARRAY-SIZE-HANDLING")
        if child is not None:
            array_size_handling_value = ArraySizeHandlingEnum.deserialize(child)
            obj.array_size_handling = array_size_handling_value

        # Parse array_size_semantics
        child = SerializationHelper.find_child_element(element, "ARRAY-SIZE-SEMANTICS")
        if child is not None:
            array_size_semantics_value = ArraySizeSemanticsEnum.deserialize(child)
            obj.array_size_semantics = array_size_semantics_value

        # Parse index_data_type_ref
        child = SerializationHelper.find_child_element(element, "INDEX-DATA-TYPE-REF")
        if child is not None:
            index_data_type_ref_value = ARRef.deserialize(child)
            obj.index_data_type_ref = index_data_type_ref_value

        # Parse max_number_of_elements
        child = SerializationHelper.find_child_element(element, "MAX-NUMBER-OF-ELEMENTS")
        if child is not None:
            max_number_of_elements_value = child.text
            obj.max_number_of_elements = max_number_of_elements_value

        return obj



class ApplicationArrayElementBuilder:
    """Builder for ApplicationArrayElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationArrayElement = ApplicationArrayElement()

    def build(self) -> ApplicationArrayElement:
        """Build and return ApplicationArrayElement object.

        Returns:
            ApplicationArrayElement instance
        """
        # TODO: Add validation
        return self._obj

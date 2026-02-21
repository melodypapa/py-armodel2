"""DataTypeMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 232)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2015)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



class DataTypeMap(ARObject):
    """AUTOSAR DataTypeMap."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_data_type_ref: Optional[ARRef]
    implementation_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataTypeMap."""
        super().__init__()
        self.application_data_type_ref: Optional[ARRef] = None
        self.implementation_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DataTypeMap to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataTypeMap, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application_data_type_ref
        if self.application_data_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.application_data_type_ref, "ApplicationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION-DATA-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize implementation_ref
        if self.implementation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.implementation_ref, "AbstractImplementationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTypeMap":
        """Deserialize XML element to DataTypeMap object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataTypeMap object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataTypeMap, cls).deserialize(element)

        # Parse application_data_type_ref
        child = SerializationHelper.find_child_element(element, "APPLICATION-DATA-TYPE-REF")
        if child is not None:
            application_data_type_ref_value = ARRef.deserialize(child)
            obj.application_data_type_ref = application_data_type_ref_value

        # Parse implementation_ref
        child = SerializationHelper.find_child_element(element, "IMPLEMENTATION-REF")
        if child is not None:
            implementation_ref_value = ARRef.deserialize(child)
            obj.implementation_ref = implementation_ref_value

        return obj



class DataTypeMapBuilder:
    """Builder for DataTypeMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTypeMap = DataTypeMap()

    def build(self) -> DataTypeMap:
        """Build and return DataTypeMap object.

        Returns:
            DataTypeMap instance
        """
        # TODO: Add validation
        return self._obj

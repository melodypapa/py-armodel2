"""DataTypeMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 232)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2015)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    application_data_type: Optional[ApplicationDataType]
    implementation: Optional[AbstractImplementationDataType]
    def __init__(self) -> None:
        """Initialize DataTypeMap."""
        super().__init__()
        self.application_data_type: Optional[ApplicationDataType] = None
        self.implementation: Optional[AbstractImplementationDataType] = None
    def serialize(self) -> ET.Element:
        """Serialize DataTypeMap to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize application_data_type
        if self.application_data_type is not None:
            serialized = ARObject._serialize_item(self.application_data_type, "ApplicationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION-DATA-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize implementation
        if self.implementation is not None:
            serialized = ARObject._serialize_item(self.implementation, "AbstractImplementationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse application_data_type
        child = ARObject._find_child_element(element, "APPLICATION-DATA-TYPE")
        if child is not None:
            application_data_type_value = ARObject._deserialize_by_tag(child, "ApplicationDataType")
            obj.application_data_type = application_data_type_value

        # Parse implementation
        child = ARObject._find_child_element(element, "IMPLEMENTATION")
        if child is not None:
            implementation_value = ARObject._deserialize_by_tag(child, "AbstractImplementationDataType")
            obj.implementation = implementation_value

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

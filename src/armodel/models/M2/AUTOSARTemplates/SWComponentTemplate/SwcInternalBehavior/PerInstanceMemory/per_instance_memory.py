"""PerInstanceMemory AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 597)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PerInstanceMemory.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    String,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class PerInstanceMemory(Identifiable):
    """AUTOSAR PerInstanceMemory."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    init_value: Optional[String]
    sw_data_def: Optional[SwDataDefProps]
    type: Optional[CIdentifier]
    type_definition: Optional[String]
    def __init__(self) -> None:
        """Initialize PerInstanceMemory."""
        super().__init__()
        self.init_value: Optional[String] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.type: Optional[CIdentifier] = None
        self.type_definition: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize PerInstanceMemory to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PerInstanceMemory, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize init_value
        if self.init_value is not None:
            serialized = ARObject._serialize_item(self.init_value, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INIT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_data_def
        if self.sw_data_def is not None:
            serialized = ARObject._serialize_item(self.sw_data_def, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type
        if self.type is not None:
            serialized = ARObject._serialize_item(self.type, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type_definition
        if self.type_definition is not None:
            serialized = ARObject._serialize_item(self.type_definition, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-DEFINITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PerInstanceMemory":
        """Deserialize XML element to PerInstanceMemory object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PerInstanceMemory object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PerInstanceMemory, cls).deserialize(element)

        # Parse init_value
        child = ARObject._find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = child.text
            obj.init_value = init_value_value

        # Parse sw_data_def
        child = ARObject._find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        # Parse type
        child = ARObject._find_child_element(element, "TYPE")
        if child is not None:
            type_value = ARObject._deserialize_by_tag(child, "CIdentifier")
            obj.type = type_value

        # Parse type_definition
        child = ARObject._find_child_element(element, "TYPE-DEFINITION")
        if child is not None:
            type_definition_value = child.text
            obj.type_definition = type_definition_value

        return obj



class PerInstanceMemoryBuilder:
    """Builder for PerInstanceMemory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PerInstanceMemory = PerInstanceMemory()

    def build(self) -> PerInstanceMemory:
        """Build and return PerInstanceMemory object.

        Returns:
            PerInstanceMemory instance
        """
        # TODO: Add validation
        return self._obj

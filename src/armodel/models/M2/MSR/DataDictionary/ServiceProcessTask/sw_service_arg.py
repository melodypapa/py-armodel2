"""SwServiceArg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 38)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1006)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 472)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 215)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_ServiceProcessTask.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ArgumentDirectionEnum,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class SwServiceArg(Identifiable):
    """AUTOSAR SwServiceArg."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    direction: Optional[ArgumentDirectionEnum]
    sw_arraysize_ref: Optional[ARRef]
    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize SwServiceArg."""
        super().__init__()
        self.direction: Optional[ArgumentDirectionEnum] = None
        self.sw_arraysize_ref: Optional[ARRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize SwServiceArg to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwServiceArg, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direction
        if self.direction is not None:
            serialized = SerializationHelper.serialize_item(self.direction, "ArgumentDirectionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_arraysize_ref
        if self.sw_arraysize_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_arraysize_ref, "ValueList")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-ARRAYSIZE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_data_def
        if self.sw_data_def is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_def, "SwDataDefProps")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwServiceArg":
        """Deserialize XML element to SwServiceArg object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwServiceArg object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwServiceArg, cls).deserialize(element)

        # Parse direction
        child = SerializationHelper.find_child_element(element, "DIRECTION")
        if child is not None:
            direction_value = ArgumentDirectionEnum.deserialize(child)
            obj.direction = direction_value

        # Parse sw_arraysize_ref
        child = SerializationHelper.find_child_element(element, "SW-ARRAYSIZE-REF")
        if child is not None:
            sw_arraysize_ref_value = ARRef.deserialize(child)
            obj.sw_arraysize_ref = sw_arraysize_ref_value

        # Parse sw_data_def
        child = SerializationHelper.find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = SerializationHelper.deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        return obj



class SwServiceArgBuilder:
    """Builder for SwServiceArg."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwServiceArg = SwServiceArg()

    def build(self) -> SwServiceArg:
        """Build and return SwServiceArg object.

        Returns:
            SwServiceArg instance
        """
        # TODO: Add validation
        return self._obj

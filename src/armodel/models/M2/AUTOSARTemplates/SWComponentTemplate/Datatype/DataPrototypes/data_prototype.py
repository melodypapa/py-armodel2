"""DataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 305)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2013)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from abc import ABC, abstractmethod


class DataPrototype(Identifiable, ABC):
    """AUTOSAR DataPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize DataPrototype."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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
    def deserialize(cls, element: ET.Element) -> "DataPrototype":
        """Deserialize XML element to DataPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototype, cls).deserialize(element)

        # Parse sw_data_def
        child = SerializationHelper.find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = SerializationHelper.deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        return obj



class DataPrototypeBuilder:
    """Builder for DataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototype = DataPrototype()

    def build(self) -> DataPrototype:
        """Build and return DataPrototype object.

        Returns:
            DataPrototype instance
        """
        # TODO: Add validation
        return self._obj

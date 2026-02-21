"""AutosarDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 231)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2001)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from abc import ABC, abstractmethod


class AutosarDataType(ARElement, ABC):
    """AUTOSAR AutosarDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    sw_data_def_props: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize AutosarDataType."""
        super().__init__()
        self.sw_data_def_props: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize AutosarDataType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AutosarDataType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_data_def_props
        if self.sw_data_def_props is not None:
            serialized = ARObject._serialize_item(self.sw_data_def_props, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarDataType":
        """Deserialize XML element to AutosarDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AutosarDataType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AutosarDataType, cls).deserialize(element)

        # Parse sw_data_def_props
        child = ARObject._find_child_element(element, "SW-DATA-DEF-PROPS")
        if child is not None:
            sw_data_def_props_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def_props = sw_data_def_props_value

        return obj



class AutosarDataTypeBuilder:
    """Builder for AutosarDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarDataType = AutosarDataType()

    def build(self) -> AutosarDataType:
        """Build and return AutosarDataType object.

        Returns:
            AutosarDataType instance
        """
        # TODO: Add validation
        return self._obj

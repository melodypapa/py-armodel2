"""SwSystemconst AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 343)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 448)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2068)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 79)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 234)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_SystemConstant.classes.json"""

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



class SwSystemconst(ARElement):
    """AUTOSAR SwSystemconst."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize SwSystemconst."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize SwSystemconst to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwSystemconst, self).serialize()

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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwSystemconst":
        """Deserialize XML element to SwSystemconst object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwSystemconst object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwSystemconst, cls).deserialize(element)

        # Parse sw_data_def
        child = ARObject._find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        return obj



class SwSystemconstBuilder:
    """Builder for SwSystemconst."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconst = SwSystemconst()

    def build(self) -> SwSystemconst:
        """Build and return SwSystemconst object.

        Returns:
            SwSystemconst instance
        """
        # TODO: Add validation
        return self._obj

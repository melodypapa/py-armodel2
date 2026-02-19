"""SwCalprmAxisSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 351)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_CalibrationParameter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis import (
    SwCalprmAxis,
)


class SwCalprmAxisSet(ARObject):
    """AUTOSAR SwCalprmAxisSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_calprm_axises: list[SwCalprmAxis]
    def __init__(self) -> None:
        """Initialize SwCalprmAxisSet."""
        super().__init__()
        self.sw_calprm_axises: list[SwCalprmAxis] = []
    def serialize(self) -> ET.Element:
        """Serialize SwCalprmAxisSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize sw_calprm_axises (list to container "SW-CALPRM-AXISES")
        if self.sw_calprm_axises:
            wrapper = ET.Element("SW-CALPRM-AXISES")
            for item in self.sw_calprm_axises:
                serialized = ARObject._serialize_item(item, "SwCalprmAxis")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwCalprmAxisSet":
        """Deserialize XML element to SwCalprmAxisSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwCalprmAxisSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_calprm_axises (list from container "SW-CALPRM-AXISES")
        obj.sw_calprm_axises = []
        container = ARObject._find_child_element(element, "SW-CALPRM-AXISES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_calprm_axises.append(child_value)

        return obj



class SwCalprmAxisSetBuilder:
    """Builder for SwCalprmAxisSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwCalprmAxisSet = SwCalprmAxisSet()

    def build(self) -> SwCalprmAxisSet:
        """Build and return SwCalprmAxisSet object.

        Returns:
            SwCalprmAxisSet instance
        """
        # TODO: Add validation
        return self._obj

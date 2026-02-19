"""DdsReliability AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 534)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsReliabilityKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsReliability(ARObject):
    """AUTOSAR DdsReliability."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    reliability_kind: Optional[DdsReliabilityKindEnum]
    reliability_max: Optional[Float]
    def __init__(self) -> None:
        """Initialize DdsReliability."""
        super().__init__()
        self.reliability_kind: Optional[DdsReliabilityKindEnum] = None
        self.reliability_max: Optional[Float] = None
    def serialize(self) -> ET.Element:
        """Serialize DdsReliability to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize reliability_kind
        if self.reliability_kind is not None:
            serialized = ARObject._serialize_item(self.reliability_kind, "DdsReliabilityKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELIABILITY-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reliability_max
        if self.reliability_max is not None:
            serialized = ARObject._serialize_item(self.reliability_max, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELIABILITY-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsReliability":
        """Deserialize XML element to DdsReliability object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsReliability object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse reliability_kind
        child = ARObject._find_child_element(element, "RELIABILITY-KIND")
        if child is not None:
            reliability_kind_value = DdsReliabilityKindEnum.deserialize(child)
            obj.reliability_kind = reliability_kind_value

        # Parse reliability_max
        child = ARObject._find_child_element(element, "RELIABILITY-MAX")
        if child is not None:
            reliability_max_value = child.text
            obj.reliability_max = reliability_max_value

        return obj



class DdsReliabilityBuilder:
    """Builder for DdsReliability."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsReliability = DdsReliability()

    def build(self) -> DdsReliability:
        """Build and return DdsReliability object.

        Returns:
            DdsReliability instance
        """
        # TODO: Add validation
        return self._obj

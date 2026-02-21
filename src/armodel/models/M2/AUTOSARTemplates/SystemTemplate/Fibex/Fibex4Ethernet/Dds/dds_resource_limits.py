"""DdsResourceLimits AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 537)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsResourceLimits(ARObject):
    """AUTOSAR DdsResourceLimits."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_instances: Optional[PositiveInteger]
    max_samples: Optional[PositiveInteger]
    max_samples_per_instance: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsResourceLimits."""
        super().__init__()
        self.max_instances: Optional[PositiveInteger] = None
        self.max_samples: Optional[PositiveInteger] = None
        self.max_samples_per_instance: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsResourceLimits to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize max_instances
        if self.max_instances is not None:
            serialized = SerializationHelper.serialize_item(self.max_instances, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-INSTANCES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_samples
        if self.max_samples is not None:
            serialized = SerializationHelper.serialize_item(self.max_samples, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SAMPLES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_samples_per_instance
        if self.max_samples_per_instance is not None:
            serialized = SerializationHelper.serialize_item(self.max_samples_per_instance, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SAMPLES-PER-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsResourceLimits":
        """Deserialize XML element to DdsResourceLimits object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsResourceLimits object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse max_instances
        child = SerializationHelper.find_child_element(element, "MAX-INSTANCES")
        if child is not None:
            max_instances_value = child.text
            obj.max_instances = max_instances_value

        # Parse max_samples
        child = SerializationHelper.find_child_element(element, "MAX-SAMPLES")
        if child is not None:
            max_samples_value = child.text
            obj.max_samples = max_samples_value

        # Parse max_samples_per_instance
        child = SerializationHelper.find_child_element(element, "MAX-SAMPLES-PER-INSTANCE")
        if child is not None:
            max_samples_per_instance_value = child.text
            obj.max_samples_per_instance = max_samples_per_instance_value

        return obj



class DdsResourceLimitsBuilder:
    """Builder for DdsResourceLimits."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsResourceLimits = DdsResourceLimits()

    def build(self) -> DdsResourceLimits:
        """Build and return DdsResourceLimits object.

        Returns:
            DdsResourceLimits instance
        """
        # TODO: Add validation
        return self._obj

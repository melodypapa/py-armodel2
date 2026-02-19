"""DelegatedPortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 162)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    SignalFanEnum,
)


class DelegatedPortAnnotation(GeneralAnnotation):
    """AUTOSAR DelegatedPortAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    signal_fan: Optional[SignalFanEnum]
    def __init__(self) -> None:
        """Initialize DelegatedPortAnnotation."""
        super().__init__()
        self.signal_fan: Optional[SignalFanEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize DelegatedPortAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DelegatedPortAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize signal_fan
        if self.signal_fan is not None:
            serialized = ARObject._serialize_item(self.signal_fan, "SignalFanEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNAL-FAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DelegatedPortAnnotation":
        """Deserialize XML element to DelegatedPortAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DelegatedPortAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DelegatedPortAnnotation, cls).deserialize(element)

        # Parse signal_fan
        child = ARObject._find_child_element(element, "SIGNAL-FAN")
        if child is not None:
            signal_fan_value = SignalFanEnum.deserialize(child)
            obj.signal_fan = signal_fan_value

        return obj



class DelegatedPortAnnotationBuilder:
    """Builder for DelegatedPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DelegatedPortAnnotation = DelegatedPortAnnotation()

    def build(self) -> DelegatedPortAnnotation:
        """Build and return DelegatedPortAnnotation object.

        Returns:
            DelegatedPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj

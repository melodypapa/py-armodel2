"""SignalServiceTranslationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 730)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SignalServiceTranslationPropsSet(ARElement):
    """AUTOSAR SignalServiceTranslationPropsSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    signal_service_propses: list[Any]
    def __init__(self) -> None:
        """Initialize SignalServiceTranslationPropsSet."""
        super().__init__()
        self.signal_service_propses: list[Any] = []
    def serialize(self) -> ET.Element:
        """Serialize SignalServiceTranslationPropsSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalServiceTranslationPropsSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize signal_service_propses (list to container "SIGNAL-SERVICE-PROPSES")
        if self.signal_service_propses:
            wrapper = ET.Element("SIGNAL-SERVICE-PROPSES")
            for item in self.signal_service_propses:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationPropsSet":
        """Deserialize XML element to SignalServiceTranslationPropsSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationPropsSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SignalServiceTranslationPropsSet, cls).deserialize(element)

        # Parse signal_service_propses (list from container "SIGNAL-SERVICE-PROPSES")
        obj.signal_service_propses = []
        container = ARObject._find_child_element(element, "SIGNAL-SERVICE-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signal_service_propses.append(child_value)

        return obj



class SignalServiceTranslationPropsSetBuilder:
    """Builder for SignalServiceTranslationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationPropsSet = SignalServiceTranslationPropsSet()

    def build(self) -> SignalServiceTranslationPropsSet:
        """Build and return SignalServiceTranslationPropsSet object.

        Returns:
            SignalServiceTranslationPropsSet instance
        """
        # TODO: Add validation
        return self._obj

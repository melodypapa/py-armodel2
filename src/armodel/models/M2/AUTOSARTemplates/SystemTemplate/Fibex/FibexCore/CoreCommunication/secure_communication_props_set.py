"""SecureCommunicationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SecureCommunicationPropsSet(FibexElement):
    """AUTOSAR SecureCommunicationPropsSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentications: list[Any]
    freshness_propses: list[Any]
    def __init__(self) -> None:
        """Initialize SecureCommunicationPropsSet."""
        super().__init__()
        self.authentications: list[Any] = []
        self.freshness_propses: list[Any] = []
    def serialize(self) -> ET.Element:
        """Serialize SecureCommunicationPropsSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecureCommunicationPropsSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentications (list to container "AUTHENTICATIONS")
        if self.authentications:
            wrapper = ET.Element("AUTHENTICATIONS")
            for item in self.authentications:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize freshness_propses (list to container "FRESHNESS-PROPSES")
        if self.freshness_propses:
            wrapper = ET.Element("FRESHNESS-PROPSES")
            for item in self.freshness_propses:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationPropsSet":
        """Deserialize XML element to SecureCommunicationPropsSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationPropsSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecureCommunicationPropsSet, cls).deserialize(element)

        # Parse authentications (list from container "AUTHENTICATIONS")
        obj.authentications = []
        container = ARObject._find_child_element(element, "AUTHENTICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.authentications.append(child_value)

        # Parse freshness_propses (list from container "FRESHNESS-PROPSES")
        obj.freshness_propses = []
        container = ARObject._find_child_element(element, "FRESHNESS-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.freshness_propses.append(child_value)

        return obj



class SecureCommunicationPropsSetBuilder:
    """Builder for SecureCommunicationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationPropsSet = SecureCommunicationPropsSet()

    def build(self) -> SecureCommunicationPropsSet:
        """Build and return SecureCommunicationPropsSet object.

        Returns:
            SecureCommunicationPropsSet instance
        """
        # TODO: Add validation
        return self._obj

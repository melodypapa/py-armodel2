"""PortInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 87)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2046)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 27)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 457)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceProviderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class PortInterface(ARElement, ABC):
    """AUTOSAR PortInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    is_service: Optional[Boolean]
    service_kind: Optional[ServiceProviderEnum]
    def __init__(self) -> None:
        """Initialize PortInterface."""
        super().__init__()
        self.is_service: Optional[Boolean] = None
        self.service_kind: Optional[ServiceProviderEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize PortInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize is_service
        if self.is_service is not None:
            serialized = ARObject._serialize_item(self.is_service, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_kind
        if self.service_kind is not None:
            serialized = ARObject._serialize_item(self.service_kind, "ServiceProviderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortInterface":
        """Deserialize XML element to PortInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortInterface, cls).deserialize(element)

        # Parse is_service
        child = ARObject._find_child_element(element, "IS-SERVICE")
        if child is not None:
            is_service_value = child.text
            obj.is_service = is_service_value

        # Parse service_kind
        child = ARObject._find_child_element(element, "SERVICE-KIND")
        if child is not None:
            service_kind_value = ServiceProviderEnum.deserialize(child)
            obj.service_kind = service_kind_value

        return obj



class PortInterfaceBuilder:
    """Builder for PortInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInterface = PortInterface()

    def build(self) -> PortInterface:
        """Build and return PortInterface object.

        Returns:
            PortInterface instance
        """
        # TODO: Add validation
        return self._obj

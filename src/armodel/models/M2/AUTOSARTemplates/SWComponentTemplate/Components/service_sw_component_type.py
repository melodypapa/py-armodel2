"""ServiceSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 336)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 306)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 659)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2056)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ServiceSwComponentType(AtomicSwComponentType):
    """AUTOSAR ServiceSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ServiceSwComponentType."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize ServiceSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ServiceSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServiceSwComponentType":
        """Deserialize XML element to ServiceSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServiceSwComponentType object
        """
        # Delegate to parent class to handle inherited attributes
        return super(ServiceSwComponentType, cls).deserialize(element)



class ServiceSwComponentTypeBuilder:
    """Builder for ServiceSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceSwComponentType = ServiceSwComponentType()

    def build(self) -> ServiceSwComponentType:
        """Build and return ServiceSwComponentType object.

        Returns:
            ServiceSwComponentType instance
        """
        # TODO: Add validation
        return self._obj

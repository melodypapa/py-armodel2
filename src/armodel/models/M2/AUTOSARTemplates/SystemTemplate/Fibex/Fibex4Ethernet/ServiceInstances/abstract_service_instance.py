"""AbstractServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 476)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_activation_routing_group import (
    PduActivationRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.so_ad_routing_group import (
    SoAdRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue.tag_with_optional_value import (
    TagWithOptionalValue,
)
from abc import ABC, abstractmethod


class AbstractServiceInstance(Identifiable, ABC):
    """AUTOSAR AbstractServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    capabilities: list[TagWithOptionalValue]
    major_version: Optional[PositiveInteger]
    method: Optional[PduActivationRoutingGroup]
    routing_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize AbstractServiceInstance."""
        super().__init__()
        self.capabilities: list[TagWithOptionalValue] = []
        self.major_version: Optional[PositiveInteger] = None
        self.method: Optional[PduActivationRoutingGroup] = None
        self.routing_group_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractServiceInstance":
        """Deserialize XML element to AbstractServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractServiceInstance object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse capabilities (list)
        obj.capabilities = []
        for child in ARObject._find_all_child_elements(element, "CAPABILITIES"):
            capabilities_value = ARObject._deserialize_by_tag(child, "TagWithOptionalValue")
            obj.capabilities.append(capabilities_value)

        # Parse major_version
        child = ARObject._find_child_element(element, "MAJOR-VERSION")
        if child is not None:
            major_version_value = child.text
            obj.major_version = major_version_value

        # Parse method
        child = ARObject._find_child_element(element, "METHOD")
        if child is not None:
            method_value = ARObject._deserialize_by_tag(child, "PduActivationRoutingGroup")
            obj.method = method_value

        # Parse routing_group_refs (list)
        obj.routing_group_refs = []
        for child in ARObject._find_all_child_elements(element, "ROUTING-GROUPS"):
            routing_group_refs_value = ARObject._deserialize_by_tag(child, "SoAdRoutingGroup")
            obj.routing_group_refs.append(routing_group_refs_value)

        return obj



class AbstractServiceInstanceBuilder:
    """Builder for AbstractServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractServiceInstance = AbstractServiceInstance()

    def build(self) -> AbstractServiceInstance:
        """Build and return AbstractServiceInstance object.

        Returns:
            AbstractServiceInstance instance
        """
        # TODO: Add validation
        return self._obj

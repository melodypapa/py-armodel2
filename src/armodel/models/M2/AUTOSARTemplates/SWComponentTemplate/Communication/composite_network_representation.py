"""CompositeNetworkRepresentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CompositeNetworkRepresentation(ARObject):
    """AUTOSAR CompositeNetworkRepresentation."""

    leaf_element_element_in_port_interface_instance_ref: Optional[Any]
    network_representation: Optional[Any]
    def __init__(self) -> None:
        """Initialize CompositeNetworkRepresentation."""
        super().__init__()
        self.leaf_element_element_in_port_interface_instance_ref: Optional[Any] = None
        self.network_representation: Optional[Any] = None


class CompositeNetworkRepresentationBuilder:
    """Builder for CompositeNetworkRepresentation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompositeNetworkRepresentation = CompositeNetworkRepresentation()

    def build(self) -> CompositeNetworkRepresentation:
        """Build and return CompositeNetworkRepresentation object.

        Returns:
            CompositeNetworkRepresentation instance
        """
        # TODO: Add validation
        return self._obj

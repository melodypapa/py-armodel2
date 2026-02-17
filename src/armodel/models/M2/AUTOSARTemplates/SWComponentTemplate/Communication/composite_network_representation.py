"""CompositeNetworkRepresentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CompositeNetworkRepresentation(ARObject):
    """AUTOSAR CompositeNetworkRepresentation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "leaf_element_element_in_port_interface_instance_ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ApplicationComposite),
        ),  # leafElementElementInPortInterfaceInstanceRef
        "network_representation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwDataDefPropsRepresentation),
        ),  # networkRepresentation
    }

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

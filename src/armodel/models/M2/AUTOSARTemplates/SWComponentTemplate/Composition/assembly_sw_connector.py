"""AssemblySwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 289)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 423)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)


class AssemblySwConnector(SwConnector):
    """AUTOSAR AssemblySwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provider_instance_ref: Optional[AbstractProvidedPortPrototype]
    requester_instance_ref: Optional[AbstractRequiredPortPrototype]
    def __init__(self) -> None:
        """Initialize AssemblySwConnector."""
        super().__init__()
        self.provider_instance_ref: Optional[AbstractProvidedPortPrototype] = None
        self.requester_instance_ref: Optional[AbstractRequiredPortPrototype] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AssemblySwConnector":
        """Deserialize XML element to AssemblySwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AssemblySwConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse provider_instance_ref
        child = ARObject._find_child_element(element, "PROVIDER-INSTANCE-REF")
        if child is not None:
            provider_instance_ref_value = ARObject._deserialize_by_tag(child, "AbstractProvidedPortPrototype")
            obj.provider_instance_ref = provider_instance_ref_value

        # Parse requester_instance_ref
        child = ARObject._find_child_element(element, "REQUESTER-INSTANCE-REF")
        if child is not None:
            requester_instance_ref_value = ARObject._deserialize_by_tag(child, "AbstractRequiredPortPrototype")
            obj.requester_instance_ref = requester_instance_ref_value

        return obj



class AssemblySwConnectorBuilder:
    """Builder for AssemblySwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssemblySwConnector = AssemblySwConnector()

    def build(self) -> AssemblySwConnector:
        """Build and return AssemblySwConnector object.

        Returns:
            AssemblySwConnector instance
        """
        # TODO: Add validation
        return self._obj

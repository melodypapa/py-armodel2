"""OperationInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1001)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_InstanceRefs.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class OperationInSystemInstanceRef(ARObject):
    """AUTOSAR OperationInSystemInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=System,
        ),  # base
        "context": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RootSwCompositionPrototype,
        ),  # context
        "context_port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=PortPrototype,
        ),  # contextPort
        "target_operation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientServerOperation,
        ),  # targetOperation
    }

    def __init__(self) -> None:
        """Initialize OperationInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.context: Optional[RootSwCompositionPrototype] = None
        self.context_port: PortPrototype = None
        self.target_operation: Optional[ClientServerOperation] = None


class OperationInSystemInstanceRefBuilder:
    """Builder for OperationInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OperationInSystemInstanceRef = OperationInSystemInstanceRef()

    def build(self) -> OperationInSystemInstanceRef:
        """Build and return OperationInSystemInstanceRef object.

        Returns:
            OperationInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj

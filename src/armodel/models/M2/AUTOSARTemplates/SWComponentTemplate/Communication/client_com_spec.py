"""ClientComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientComSpec(RPortComSpec):
    """AUTOSAR ClientComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    end_to_end_call: Optional[TimeValue]
    operation: Optional[ClientServerOperation]
    transformation_coms: list[Any]
    def __init__(self) -> None:
        """Initialize ClientComSpec."""
        super().__init__()
        self.end_to_end_call: Optional[TimeValue] = None
        self.operation: Optional[ClientServerOperation] = None
        self.transformation_coms: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientComSpec":
        """Deserialize XML element to ClientComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientComSpec object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse end_to_end_call
        child = ARObject._find_child_element(element, "END-TO-END-CALL")
        if child is not None:
            end_to_end_call_value = child.text
            obj.end_to_end_call = end_to_end_call_value

        # Parse operation
        child = ARObject._find_child_element(element, "OPERATION")
        if child is not None:
            operation_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.operation = operation_value

        # Parse transformation_coms (list)
        obj.transformation_coms = []
        for child in ARObject._find_all_child_elements(element, "TRANSFORMATION-COMS"):
            transformation_coms_value = child.text
            obj.transformation_coms.append(transformation_coms_value)

        return obj



class ClientComSpecBuilder:
    """Builder for ClientComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientComSpec = ClientComSpec()

    def build(self) -> ClientComSpec:
        """Build and return ClientComSpec object.

        Returns:
            ClientComSpec instance
        """
        # TODO: Add validation
        return self._obj

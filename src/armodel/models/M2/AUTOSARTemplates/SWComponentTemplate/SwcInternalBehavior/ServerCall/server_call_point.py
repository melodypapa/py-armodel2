"""ServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 335)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 580)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2055)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from abc import ABC, abstractmethod


class ServerCallPoint(AbstractAccessPoint, ABC):
    """AUTOSAR ServerCallPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    operation_instance_ref: Optional[ClientServerOperation]
    timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize ServerCallPoint."""
        super().__init__()
        self.operation_instance_ref: Optional[ClientServerOperation] = None
        self.timeout: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServerCallPoint":
        """Deserialize XML element to ServerCallPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServerCallPoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse operation_instance_ref
        child = ARObject._find_child_element(element, "OPERATION-INSTANCE-REF")
        if child is not None:
            operation_instance_ref_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.operation_instance_ref = operation_instance_ref_value

        # Parse timeout
        child = ARObject._find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = child.text
            obj.timeout = timeout_value

        return obj



class ServerCallPointBuilder:
    """Builder for ServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServerCallPoint = ServerCallPoint()

    def build(self) -> ServerCallPoint:
        """Build and return ServerCallPoint object.

        Returns:
            ServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj

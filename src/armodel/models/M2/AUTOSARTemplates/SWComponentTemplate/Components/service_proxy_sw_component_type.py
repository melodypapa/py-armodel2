"""ServiceProxySwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 661)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2056)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ServiceProxySwComponentType(AtomicSwComponentType):
    """AUTOSAR ServiceProxySwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ServiceProxySwComponentType."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServiceProxySwComponentType":
        """Deserialize XML element to ServiceProxySwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServiceProxySwComponentType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class ServiceProxySwComponentTypeBuilder:
    """Builder for ServiceProxySwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceProxySwComponentType = ServiceProxySwComponentType()

    def build(self) -> ServiceProxySwComponentType:
        """Build and return ServiceProxySwComponentType object.

        Returns:
            ServiceProxySwComponentType instance
        """
        # TODO: Add validation
        return self._obj

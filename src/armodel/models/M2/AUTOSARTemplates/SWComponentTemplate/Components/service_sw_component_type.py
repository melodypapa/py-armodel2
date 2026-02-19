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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServiceSwComponentType":
        """Deserialize XML element to ServiceSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServiceSwComponentType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



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

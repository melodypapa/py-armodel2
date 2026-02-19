"""ArgumentDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 303)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 300)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 102)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1998)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 29)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ArgumentDirectionEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ServerArgumentImplPolicyEnum,
)


class ArgumentDataPrototype(AutosarDataPrototype):
    """AUTOSAR ArgumentDataPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    direction: Optional[ArgumentDirectionEnum]
    server_argument_impl: Optional[ServerArgumentImplPolicyEnum]
    def __init__(self) -> None:
        """Initialize ArgumentDataPrototype."""
        super().__init__()
        self.direction: Optional[ArgumentDirectionEnum] = None
        self.server_argument_impl: Optional[ServerArgumentImplPolicyEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArgumentDataPrototype":
        """Deserialize XML element to ArgumentDataPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArgumentDataPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ArgumentDataPrototype, cls).deserialize(element)

        # Parse direction
        child = ARObject._find_child_element(element, "DIRECTION")
        if child is not None:
            direction_value = ArgumentDirectionEnum.deserialize(child)
            obj.direction = direction_value

        # Parse server_argument_impl
        child = ARObject._find_child_element(element, "SERVER-ARGUMENT-IMPL")
        if child is not None:
            server_argument_impl_value = ServerArgumentImplPolicyEnum.deserialize(child)
            obj.server_argument_impl = server_argument_impl_value

        return obj



class ArgumentDataPrototypeBuilder:
    """Builder for ArgumentDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArgumentDataPrototype = ArgumentDataPrototype()

    def build(self) -> ArgumentDataPrototype:
        """Build and return ArgumentDataPrototype object.

        Returns:
            ArgumentDataPrototype instance
        """
        # TODO: Add validation
        return self._obj

"""ExecutableEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 70)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 538)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2024)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects.sw_addr_method import (
    SwAddrMethod,
)


class ExecutableEntity(Identifiable):
    """AUTOSAR ExecutableEntity."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "activations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ExecutableEntity,
        ),  # activations
        "can_enters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ExclusiveArea,
        ),  # canEnters
        "exclusive_area_nestings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ExclusiveAreaNestingOrder,
        ),  # exclusiveAreaNestings
        "minimum_start": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minimumStart
        "reentrancy_level_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ReentrancyLevelEnum,
        ),  # reentrancyLevelEnum
        "runs_insides": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ExclusiveArea,
        ),  # runsInsides
        "sw_addr_method": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwAddrMethod,
        ),  # swAddrMethod
    }

    def __init__(self) -> None:
        """Initialize ExecutableEntity."""
        super().__init__()
        self.activations: list[ExecutableEntity] = []
        self.can_enters: list[ExclusiveArea] = []
        self.exclusive_area_nestings: list[ExclusiveAreaNestingOrder] = []
        self.minimum_start: Optional[TimeValue] = None
        self.reentrancy_level_enum: Optional[ReentrancyLevelEnum] = None
        self.runs_insides: list[ExclusiveArea] = []
        self.sw_addr_method: Optional[SwAddrMethod] = None


class ExecutableEntityBuilder:
    """Builder for ExecutableEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutableEntity = ExecutableEntity()

    def build(self) -> ExecutableEntity:
        """Build and return ExecutableEntity object.

        Returns:
            ExecutableEntity instance
        """
        # TODO: Add validation
        return self._obj

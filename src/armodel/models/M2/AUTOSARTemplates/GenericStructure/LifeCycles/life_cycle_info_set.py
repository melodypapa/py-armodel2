"""LifeCycleInfoSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_info import (
    LifeCycleInfo,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state_definition_group import (
    LifeCycleStateDefinitionGroup,
)


class LifeCycleInfoSet(ARElement):
    """AUTOSAR LifeCycleInfoSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_lc_state", None, False, False, LifeCycleState),  # defaultLcState
        ("default_period", None, False, False, LifeCyclePeriod),  # defaultPeriod
        ("life_cycle_infos", None, False, True, LifeCycleInfo),  # lifeCycleInfos
        ("used_life_cycle", None, False, False, LifeCycleStateDefinitionGroup),  # usedLifeCycle
    ]

    def __init__(self) -> None:
        """Initialize LifeCycleInfoSet."""
        super().__init__()
        self.default_lc_state: LifeCycleState = None
        self.default_period: Optional[LifeCyclePeriod] = None
        self.life_cycle_infos: list[LifeCycleInfo] = []
        self.used_life_cycle: LifeCycleStateDefinitionGroup = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LifeCycleInfoSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleInfoSet":
        """Create LifeCycleInfoSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LifeCycleInfoSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LifeCycleInfoSet since parent returns ARObject
        return cast("LifeCycleInfoSet", obj)


class LifeCycleInfoSetBuilder:
    """Builder for LifeCycleInfoSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleInfoSet = LifeCycleInfoSet()

    def build(self) -> LifeCycleInfoSet:
        """Build and return LifeCycleInfoSet object.

        Returns:
            LifeCycleInfoSet instance
        """
        # TODO: Add validation
        return self._obj

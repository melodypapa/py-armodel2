"""LifeCycleInfo AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class LifeCycleInfo(ARObject):
    """AUTOSAR LifeCycleInfo."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lc_object", None, False, False, Referrable),  # lcObject
        ("lc_state", None, False, False, LifeCycleState),  # lcState
        ("period_begin", None, False, False, LifeCyclePeriod),  # periodBegin
        ("period_end", None, False, False, LifeCyclePeriod),  # periodEnd
        ("remark", None, False, False, DocumentationBlock),  # remark
        ("use_insteads", None, False, True, Referrable),  # useInsteads
    ]

    def __init__(self) -> None:
        """Initialize LifeCycleInfo."""
        super().__init__()
        self.lc_object: Referrable = None
        self.lc_state: Optional[LifeCycleState] = None
        self.period_begin: Optional[LifeCyclePeriod] = None
        self.period_end: Optional[LifeCyclePeriod] = None
        self.remark: Optional[DocumentationBlock] = None
        self.use_insteads: list[Referrable] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LifeCycleInfo to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleInfo":
        """Create LifeCycleInfo from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LifeCycleInfo instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LifeCycleInfo since parent returns ARObject
        return cast("LifeCycleInfo", obj)


class LifeCycleInfoBuilder:
    """Builder for LifeCycleInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleInfo = LifeCycleInfo()

    def build(self) -> LifeCycleInfo:
        """Build and return LifeCycleInfo object.

        Returns:
            LifeCycleInfo instance
        """
        # TODO: Add validation
        return self._obj

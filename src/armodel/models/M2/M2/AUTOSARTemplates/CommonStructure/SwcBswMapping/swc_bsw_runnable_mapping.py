"""SwcBswRunnableMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)


class SwcBswRunnableMapping(ARObject):
    """AUTOSAR SwcBswRunnableMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bsw_entity": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleEntity,
        ),  # bswEntity
        "swc_runnable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RunnableEntity,
        ),  # swcRunnable
    }

    def __init__(self) -> None:
        """Initialize SwcBswRunnableMapping."""
        super().__init__()
        self.bsw_entity: Optional[BswModuleEntity] = None
        self.swc_runnable: Optional[RunnableEntity] = None


class SwcBswRunnableMappingBuilder:
    """Builder for SwcBswRunnableMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswRunnableMapping = SwcBswRunnableMapping()

    def build(self) -> SwcBswRunnableMapping:
        """Build and return SwcBswRunnableMapping object.

        Returns:
            SwcBswRunnableMapping instance
        """
        # TODO: Add validation
        return self._obj

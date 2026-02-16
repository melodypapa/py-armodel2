"""PerInstanceMemorySize AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)


class PerInstanceMemorySize(ARObject):
    """AUTOSAR PerInstanceMemorySize."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "alignment": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # alignment
        "per_instance_memory_memory": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PerInstanceMemory,
        ),  # perInstanceMemoryMemory
        "size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # size
    }

    def __init__(self) -> None:
        """Initialize PerInstanceMemorySize."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.per_instance_memory_memory: Optional[PerInstanceMemory] = None
        self.size: Optional[PositiveInteger] = None


class PerInstanceMemorySizeBuilder:
    """Builder for PerInstanceMemorySize."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PerInstanceMemorySize = PerInstanceMemorySize()

    def build(self) -> PerInstanceMemorySize:
        """Build and return PerInstanceMemorySize object.

        Returns:
            PerInstanceMemorySize instance
        """
        # TODO: Add validation
        return self._obj

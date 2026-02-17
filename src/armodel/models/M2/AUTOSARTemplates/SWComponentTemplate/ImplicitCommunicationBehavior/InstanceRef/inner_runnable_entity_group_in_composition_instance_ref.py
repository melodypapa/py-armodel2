"""InnerRunnableEntityGroupInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 956)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.runnable_entity_group import (
    RunnableEntityGroup,
)


class InnerRunnableEntityGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerRunnableEntityGroupInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompositionSwComponentType,
        ),  # base
        "context_sws": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SwComponent),
        ),  # contextSws
        "target_runnable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=RunnableEntityGroup,
        ),  # targetRunnable
    }

    def __init__(self) -> None:
        """Initialize InnerRunnableEntityGroupInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_sws: list[Any] = []
        self.target_runnable: RunnableEntityGroup = None


class InnerRunnableEntityGroupInCompositionInstanceRefBuilder:
    """Builder for InnerRunnableEntityGroupInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InnerRunnableEntityGroupInCompositionInstanceRef = InnerRunnableEntityGroupInCompositionInstanceRef()

    def build(self) -> InnerRunnableEntityGroupInCompositionInstanceRef:
        """Build and return InnerRunnableEntityGroupInCompositionInstanceRef object.

        Returns:
            InnerRunnableEntityGroupInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj

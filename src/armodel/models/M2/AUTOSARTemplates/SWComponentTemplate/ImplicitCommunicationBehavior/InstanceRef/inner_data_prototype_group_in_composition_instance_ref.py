"""InnerDataPrototypeGroupInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 954)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
    DataPrototypeGroup,
)


class InnerDataPrototypeGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerDataPrototypeGroupInCompositionInstanceRef."""

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
        "target_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataPrototypeGroup,
        ),  # targetData
    }

    def __init__(self) -> None:
        """Initialize InnerDataPrototypeGroupInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_sws: list[Any] = []
        self.target_data: Optional[DataPrototypeGroup] = None


class InnerDataPrototypeGroupInCompositionInstanceRefBuilder:
    """Builder for InnerDataPrototypeGroupInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InnerDataPrototypeGroupInCompositionInstanceRef = InnerDataPrototypeGroupInCompositionInstanceRef()

    def build(self) -> InnerDataPrototypeGroupInCompositionInstanceRef:
        """Build and return InnerDataPrototypeGroupInCompositionInstanceRef object.

        Returns:
            InnerDataPrototypeGroupInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj

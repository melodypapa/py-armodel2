"""ApplicationCompositeElementInPortInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 952)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)


class ApplicationCompositeElementInPortInterfaceInstanceRef(ARObject):
    """AUTOSAR ApplicationCompositeElementInPortInterfaceInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataInterface,
        ),  # base
        "context_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (ApplicationComposite),
        ),  # contextDatas
        "root_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarDataPrototype,
        ),  # rootData
        "target_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ApplicationComposite),
        ),  # targetData
    }

    def __init__(self) -> None:
        """Initialize ApplicationCompositeElementInPortInterfaceInstanceRef."""
        super().__init__()
        self.base: Optional[DataInterface] = None
        self.context_datas: list[Any] = []
        self.root_data: Optional[AutosarDataPrototype] = None
        self.target_data: Optional[Any] = None


class ApplicationCompositeElementInPortInterfaceInstanceRefBuilder:
    """Builder for ApplicationCompositeElementInPortInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeElementInPortInterfaceInstanceRef = ApplicationCompositeElementInPortInterfaceInstanceRef()

    def build(self) -> ApplicationCompositeElementInPortInterfaceInstanceRef:
        """Build and return ApplicationCompositeElementInPortInterfaceInstanceRef object.

        Returns:
            ApplicationCompositeElementInPortInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj

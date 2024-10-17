import { Component, OnInit } from '@angular/core';
import { TargetsService } from '../../services/targets.service';

@Component({
  selector: 'app-targets',
  templateUrl: './targets.component.html',
  styleUrls: ['./targets.component.scss']
})
export class TargetsComponent implements OnInit {
  targets: any[] = [];
  newTarget: any = {};

  constructor(private targetsService: TargetsService) {}

  ngOnInit(): void {
    this.loadTargets();
  }

  loadTargets(): void {
    this.targetsService.getTargets().subscribe(data => {
      this.targets = data;
    });
  }

  addTarget(): void {
    this.targetsService.addTarget(this.newTarget).subscribe(() => {
      this.newTarget = {};
      this.loadTargets();
    });
  }

  deleteTarget(id: number): void {
    this.targetsService.deleteTarget(id).subscribe(() => {
      this.loadTargets();
    });
  }
}
